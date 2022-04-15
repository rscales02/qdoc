import { FC, ChangeEvent, useState } from "react";
import React from "react";

export interface IRegisterFormProps {
  route: string;
}

export interface IRegisterFormFields {
  [item: string]: string;
}

export const RegisterForm: FC<IRegisterFormProps> = (props) => {
  const [inputField, setInputField] = useState<IRegisterFormFields>({
    email: "",
    password: "",
  });
  const inputsHandler = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.currentTarget.id === "email" || e.currentTarget.id === "password") {
      setInputField({
        ...inputField,
        [e.currentTarget.id]: String(e.currentTarget.value),
      });
    }
  };
  const handleAddValue = (response: any) => {
    if (!response) return;
    localStorage.setItem("user", JSON.stringify(response));
  };
  const handleSubmit = (event: React.FormEvent) => {
    event.preventDefault();
    var queryString = Object.keys(inputField)
      .map((key: string) => key + "=" + inputField[key])
      .join("&");

    return fetch(
      `http://localhost:5000/auth/` + props.route + "?" + queryString,
      {
        mode: "cors",
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
      }
    )
      .then((response) => response.json())
      .then((response) => handleAddValue(response))
      .catch((error: any) => console.log(error));
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          id="email"
          placeholder="Email"
          value={inputField.email || ""}
          onChange={(e) => inputsHandler(e)}
        />
        <input
          type="text"
          id="password"
          placeholder="Password"
          value={inputField.password || ""}
          onChange={(e) => inputsHandler(e)}
        />
        {props.route === "register" ? (
          <input
            type="text"
            id="password_match"
            placeholder="Retype Password"
          />
        ) : (
          <div />
        )}
        <input type="submit" />
      </form>
    </div>
  );
};
