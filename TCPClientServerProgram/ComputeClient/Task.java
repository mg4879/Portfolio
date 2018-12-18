/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/**
 *
 * @author Michael Gonzalez S0292161
 */
//Task interface for interacting between client and server
public interface Task
{
    public void executeTask(); //Executes specific compute-task
    public Object getResult(); //returns result of compute-task
}
