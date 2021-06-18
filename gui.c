void init(){
	system("title=VER 1.03");
	system("color 7");
}

void start(){
	LList head = NULL;
	head = malloc(sizeof(LNode));
	head->next = NULL;
	char ch,flag = 1;
	char s[2400];
	FILE* menu = NULL;
	menu = fopen("gui/menu.txt","r+");
	
	for(int cx = 6;cx >= 0;cx--){
		fseek(menu,pos[cx],SEEK_SET);
		fputc(' ',menu);
	}
	rewind(menu);
	
	do{
		{
			fseek(menu,pos[flag-1],SEEK_SET);
			fputc('X',menu);
			rewind(menu);
		}
		system("cls");
		rewind(menu);
		fread(s,1,2200,menu);
		s[ftell(menu)] = '\0';
		printf("%s",s);
		fflush(menu);
		ch = getch();
		rewind(stdin);
		ch = tolower(ch);
		switch(ch){
			case 'w':
				{
					fseek(menu,pos[flag-1],SEEK_SET);
					fputc(' ',menu);
					rewind(menu);
				}
				flag--;
				if(!flag)flag = 7;
				break;
			case 's':
				{
					fseek(menu,pos[flag-1],SEEK_SET);
					fputc(' ',menu);
					rewind(menu);
				}
				flag++;
				if(flag > 7)flag = 1;
				break;
			case 'p':
				 if(flag == 1){
				 	A(head);
				 }else if(flag == 2){
				 	F(head);
				 }else if(flag == 3){
				 	S(head);
				 }else if(flag == 4){
				 	M(head);
				 }else if(flag == 5){
				 	head = R(head);
				 }else if(flag == 6)goto out;
				 else{
				 	stove(head);
				 }
				 break;
			default:
				printf("Incorrect choice!\n");
		}
	}while(1);
	out:fclose(menu);
}
