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

public class ComputeCircle implements Task, Serializable
{

    private double radius;
    private double area;
    private double perimeter;
    private String result;

    public ComputeCircle()
    {
    }

    public ComputeCircle(double r)
    {
        this.radius = r;
    }

    public double getRadius()
    {
        return this.radius;
    }

    public void setRadius(double radius)
    {
        this.radius = radius;
    }
    @Override
    public void executeTask()
    {
        this.area = Math.PI * (getRadius() * getRadius());
        this.perimeter = Math.PI * 2 * getRadius();
    }
    @Override
    public Object getResult()
    {
        return String.format("\nCircle Radius: %.2f   Circle Area: %.2f   Circle Perimeter:  %.2f", this.radius, this.area, this.perimeter);
    }

}
