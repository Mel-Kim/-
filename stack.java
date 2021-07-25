public class stack {

	public static void main(String[] args) {
		//TODO Auto-generated method stub
		java.util.Stack<Integer> s = new java.util.Stack<Integer>();
		
		System.out.println("Stack created");

		for(int i=0; i<10;i++) //0~9의 수로 스택구성
			s.push(new Integer(i));
			
			System.out.println("1pop:" +s.pop()); //스택의 값은 뺀다.
			System.out.println("2pop:" +s.pop()); //스택의 값은 뺀다.
			System.out.println("3pop:" +s.pop()); //스택의 값은 뺀다.
			System.out.println("4pop:" +s.pop()); //스택의 값은 뺀다.
			
			System.out.println("stack pop:" +s.peek()); //현재 스택의 위치를 보여준다.
		
	}
	
}


Stack created
1pop:9
2pop:8
3pop:7
4pop:6
stack pop:5
