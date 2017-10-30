#import <Foundation/NSObject.h>
@interface ListNode : NSObject
{
@private
  int numero;
  ListNode* next;
}

- (id) numero: (int) n_;
- (int) numero;
- (id) next: (ListNode*) ne_;
- (ListNode*) next;
- (id) initWithName:(int)nu_ next:(ListNode*)nex_;
@end
@implementation ListNode
- (id) numero: (int) n_
{
  numero = n_;
  return self;
}
- (int) numero
{
  return numero;
}
- (id) next: (ListNode*) ne_
{
  next = ne_;
  return self;
}
- (ListNode*) next
{
  return next;
}
- (id) initWithName:(int)nu_ next:(ListNode*)nex_
{
  self = [super init];
  self.numero: nu_;
  self.next: nex_;
  return self;
}
@end
int main(){
int i;
int j = 1;
printf("Enter how many values to input: ");
scanf("%s", &i);
ListNode* node;
for (j; j <= i; j++){
int q;
printf("Enter value %d", j, ": ");
scanf("%d", &q);
node = [[ListNode alloc] initWithValue: q, node];
}
for (i; i > 0; i--){
printf("%d", node.numero);
ListNode* temp = node;
node = node.next;
temp release;
}
}
