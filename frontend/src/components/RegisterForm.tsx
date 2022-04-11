import { FC } from "react";
import React from "react";
interface IRegisterFormProps {};

export const RegisterForm: FC<IRegisterFormProps> = (props) => {
    const handleSubmit = (event: React.FormEvent) => {
      // const email = event.
      // const password = event.target.password
      console.log(event.target)
      return fetch(`http://localhost:5000/auth/register`,{
            'method':'POST',
            headers : {
            'Content-Type':'application/json'
            },
            // body:JSON.stringify({'email': email, 'password': password})
        }).then(response => response.json())
        .catch(error => console.log(error))
    }

    return (
        <div>
          <form onSubmit={handleSubmit}>
            <input type='text' id='email'/>
            <input type="text" id='password'/>
            <input type="submit"/>
          </form>
        </div>
    );
}
