/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import java.io.*;
/**
 *
 * @author Michael Gonzalez S0292161
 */
public class ComputeSquare implements Task, Serializable
{

    private double side;
    private double area;
    private double perimeter;
    private String result;

    public ComputeSquare ()
    {

    }

    public ComputeSquare (double s)
    {
        this.side = s;
    }

    public double getSide ()
    {
        return this.side;
    }

    public void setSide(double s)
    {
        this.side = s;
    }

    @Override
    public void executeTask()
    {
        this.area = this.side * this.side;
        this.perimeter = 4.0 * this.side;
    }

    @Override
    public Object getResult()
    {
        return String.format("\nSquare Side: %.2f   Square Area: %.2f   Square Perimeter:  %.2f", this.side, this.area, this.perimeter);
    }

}

