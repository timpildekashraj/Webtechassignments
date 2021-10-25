import java.io.*;
import java.util.*;
import java.net.*;

public class server
{
	public static void main(String[] args) {
	    try
	    {
	        String str;
	        ServerSocket ss= new ServerSocket(2000);
	        Socket s = ss.accept();
	        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	        InputStream is = s.getInputStream();
	        DataInputStream dis = new DataInputStream(is);
	        OutputStream os = s.getOutputStream();
	        DataOutputStream dos = new DataOutputStream(os);
	        System.out.println("\n ************************************************************ \n");
	        System.out.println("\n conversation between client and server \n");
	        System.out.println("\n ************************************************************ \n");
	        System.out.println("\n To Client Enter The String : \n");

	        System.out.println("\n Client says ...... \n");
	        while(true)
	        {
	        	// System.out.println("\n Client says : \n");
	            str= br.readLine();
	            if(str.equals("end"))
	                 break;
	            dos.writeUTF(str);
	            System.out.println();
	            System.out.println(dis.readUTF());
	        }
	    }

	    catch(IOException e)
	    {
	        	System.out.println("Client Terminate");
	    }

	}
}
