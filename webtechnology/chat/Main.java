import java.io.*;
import java.util.*;
import java.net.*;

public class Main
{
	public static void main(String[] args) {
	    try
	    {
	        String str;
	        Socket s= new Socket("LocalHost",2000);
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        InputStream is= s.getInputStream();
	        DataInputStream dis = new DataInputStream(is);
	        OutputStream os = s.getOutputStream();
	        DataOutputStream dos = new DataOutputStream(os);
	        System.out.println("\n ************************************************************ \n\n");
	        System.out.println("\n conversation between client and server \n\n");
	        System.out.println("\n ************************************************************ \n");
	        System.out.println("\n To Server Enter The String : \t");

	        System.out.println("\n server says ...... \n");
	        while(true)
	        {
	            // System.out.println("\n server says : \n");
	            System.out.println(dis.readUTF());
	            System.out.println("\n");
	            str= br.readLine();
	            if(str.equals("end"))
	                 break;
	            dos.writeUTF(str);
	        }
	    }

	    catch(IOException e)
	    {
	        	System.out.println("server Terminate");
	    }

	}
}
