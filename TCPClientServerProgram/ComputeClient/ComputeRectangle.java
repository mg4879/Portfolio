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
public class ComputeRectangle implements Task, Serializable
{

    private double length;
    private double width;
    private double area;
    private double perimeter;
    private String result;

    public ComputeRectangle ()
    {

    }

    public ComputeRectangle(double l, double w)
    {
        this.length = l;
        this.width = w;
    }

    public double getLength ()
    {
        return this.length;
    }

    public void setLength(double l)
    {
        this.length = l;
    }

    public double getWidth()
    {
        return this.width;
    }

    public void setWidth(double w)
    {
        this.width = w;
    }

    @Override
    public void executeTask()
    {
        this.area = this.length * this.width;
        this.perimeter = 2.0 * (this.length + this.width);
    }

    @Override
    public Object getResult()
    {
        return String.format("\nRectangle Length: %.2f   Rectangle Width: %.2f   Rectangle Area: %.2f   Rectangle Perimeter:  %.2f", this.length, this.width, this.area, this.perimeter);
    }

}

