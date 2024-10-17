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


            sock.close();
        }
		catch (Exception e)
		{
            e.printStackTrace();
        }
    }
}

