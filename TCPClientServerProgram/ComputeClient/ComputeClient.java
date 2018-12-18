/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import java.net.*;
import java.io.*;
import java.util.Scanner;

/**
 *
 * @author Michael Gonzalez S0292161
 */
public class ComputeClient
{

    public static void main(String[] args)
    {

        Socket s = null;

        try
        {
            while(true)
            {
                final String SERVERNAME = "localhost"; //Variable to hold server name
                final int SERVERPORT = 8888;
                s = new Socket(SERVERNAME, SERVERPORT);

                ObjectInputStream in = null; //create an ObjectInputStream
                ObjectOutputStream out = null; //create an ObjectOutputStream

                out = new ObjectOutputStream(s.getOutputStream());
                in = new ObjectInputStream(s.getInputStream());

                //Display menu to user
                System.out.println("\n**************************\n"
                                   + "1.Circle\n2.Square\n3.Rectangle\n4.Exit\n"
                                   + "**************************\n");
                Scanner input = new Scanner(System.in);
                System.out.print("Enter a choice: ");
                String getChoice = input.nextLine();

                if ("1".equals(getChoice)) //if selects Circle choice
                {
                    //Set circle radius to user choice and write object
                    System.out.print("\nEnter the circles area: ");
                    double getRadius = input.nextDouble();
                    ComputeCircle circle = new ComputeCircle(getRadius);
                    circle.setRadius(getRadius);
                    out.writeObject(circle);
                }
                else if ("2".equals(getChoice)) //if user selects square choice
                {
                    //Set square area and write object
                    System.out.print("\nEnter side of square: ");
                    double getSide = input.nextDouble();
                    ComputeSquare square = new ComputeSquare(getSide);
                    square.setSide(getSide);
                    out.writeObject(square);
                }
                else if ("3".equals(getChoice)) //if user selects rectangle choice
                {
                    System.out.print("\nEnter the length of Rectangle: ");
                    double getLength = input.nextDouble();
                    System.out.print("Enter the width of Rectangle: ");
                    double getWidth = input.nextDouble();
                    ComputeRectangle rectangle = new ComputeRectangle(getLength, getWidth);
                    rectangle.setLength(getLength);
                    rectangle.setWidth(getWidth);
                    out.writeObject(rectangle);
                }
                else
                {
                    s.close();
                    System.exit(0); //exit program if user enters "4"
                }
                //reads object send from server, casts object to Task, and prints the result from server
                Object computeClient = in.readObject(); //
                Task task = (Task)computeClient;
                System.out.println(task.getResult());
            }


        }
        catch (UnknownHostException e)
        {
            System.out.println("Socket:" + e.getMessage());
        }
        catch (EOFException e)
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            System.out.println("readline:" + e.getMessage());
        }
        catch (ClassNotFoundException ex)
        {
            ex.printStackTrace();
        }
        finally
        {
            if(s != null)
                try
                {
                    s.close();
                }
                catch (IOException e)
                {
                    System.out.println("close:" + e.getMessage());
                }

        }




    }

}
