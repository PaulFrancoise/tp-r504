import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

public class ClientUDP
{
    public static void main(String[] args)
	{
        try
		{
            // Récupérer l'adresse IP locale
            InetAddress addr = InetAddress.getLocalHost();
            System.out.println("Adresse = " + addr.getHostName());

			String s = "LA CAUTION";
			byte[] data = s.getBytes(); 

			DatagramPacket packet = new DatagramPacket( data, data.length, addr, 1234 );
			DatagramSocket sock = new DatagramSocket(); 
			sock.send(packet);		

            sock.close();
        }
		catch (Exception e)
		{
            e.printStackTrace();
        }
    }
}

