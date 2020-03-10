#include<stdio.h>
#define cap 5
void push();
void pop();
void display();
int top=-1,stack[cap];
void main()
{
    int a,i;
    do
    {
    printf("WHAT TO DO ON STACK??\n\t1.Insert\n\t2.Delete\n\t3.Display\n");
    scanf("%d",&a);
    
    switch(a)
    {
        case 1:
          push();
          break;
        case 2:
          pop();
          break;
        case 3:
          display();
          break;
    }
    }while(a!=4);
}
void push()
{
    int ele;
    printf("Enter the Element to be pushed::");
    scanf("%d",&ele);
    if(top==4)
        printf("SORRY,STACK IS FULL\n");
    else
    {
        ++top;
        stack[top]=ele;
    }
}
void pop()
{
    int ele;
    if(top==-1)
        printf("SORRY,STACK IS EMPTY\n");
    else
    {
        ele=stack[top];
        top--;
        printf("%d IS REMOVED FROM STACK\n",ele);
    }
}
void display()
{
    int i;
    if(top==-1)
        printf("STACK IS EMPTY,PLS,INSERT NUMBER.\n");
    else
    {
    printf("ELEMENTS IN STACK ARE:\n");
    for(i=top;i>-1;i--)
    {
        printf("%d\tindex:%d\n",stack[i],i);
    }
    }
}
