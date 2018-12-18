/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 * @author Michael Gonzalez S0292161
 */

import java.io.*;

public class ErrorMessage implements Task, Serializable
{

    private String finalResult;

    ErrorMessage()
    {
    }

    //Override Task interface getResult() and return the final computing result
    public Object getResult()
    {

        return this.finalResult;
    }

    //Set the error message
    public void setErrorMessage(String msg)
    {
        this.finalResult = msg;
    }

    //Override Task interface executeTask() method
    @Override
    public void executeTask()
    {
    }
}
