/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import java.net.*;
import java.io.*;
/**
 *
 * @author Michael Gonzalez S0292161
 */

public class ComputeServer
{
    public static void main(String args[])
    {

        try
        {
            final int SERVERPORT = 8888; //variable to hold server port number
            ServerSocket listenSocket = new ServerSocket(SERVERPORT); //creates a new server socket

            while (true) //listen for connections
            {
                Socket clientSocket = listenSocket.accept();
                Connection c = new Connection(clientSocket);
            }

        }
        catch (IOException e)
        {
            System.out.println("Listen socket:" + e.getMessage());
        }
    }
}

class Connection extends Thread
{

    ObjectInputStream in;
    ObjectOutputStream out;
    Socket clientSocket;

    public Connection(Socket aClientSocket)
    {
        try
        {
            clientSocket = aClientSocket;
            in = new ObjectInputStream(clientSocket.getInputStream());
            out = new ObjectOutputStream(clientSocket.getOutputStream());
            this.start();


        }
        catch (IOException e)
        {
            System.out.println("Connection:" + e.getMessage());
        }
    }

    @Override
    public void run()
    {
        try
        {
            //reads in object from client, casts to task interface, and returns result to client
            Object computeClient = in.readObject(); //create Client object
            Task task = (Task)computeClient; //Cast client object to task interface
            task.executeTask(); //executes specific task sent from client
            out.writeObject(task); //send task object back to client
            System.out.println(String.format("Performing a client task of %s", task.getClass().getName()));
            //read object in and set area and perimeter



        }
        catch (EOFException e)
        {
            System.out.println("Client disconnected");
        }
        catch (IOException e)
        {
            System.out.println("readline:" + e.getMessage());
        }
        catch (ClassNotFoundException ex)
        {
            try
            {
                //displays error and sends error to client if .class definitions are missing from server folder
                ErrorMessage error = new ErrorMessage();
                error.setErrorMessage("\nUpload compute-task " + ex.getMessage() + " before calling the server!");
                System.out.println("The compute-task " + ex.getMessage() + " definition cannot be found!");
                out.writeObject(error);

            }
            catch (IOException ex1)
            {
                ex1.getMessage();
            }

        }

        finally
        {
            try
            {
                clientSocket.close();
            }
            catch (IOException e)    /*close failed*/
            {
                System.out.println("close:" + e.getMessage());
            }
        }






    }

}
