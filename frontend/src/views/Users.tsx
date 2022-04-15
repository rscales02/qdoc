import React, { useState } from "react";

const AddButon = ({ handleAddValue }: any) => {
  return <button onClick={handleAddValue}>Add</button>;
};

export const Users = (props: any) => {
  const [value, setValue] = useState("");

  const handleAddValue = (response: any) => {
    setValue(response);
  };
  fetch(`http://localhost:5000/auth/get_users`, {
    mode: "cors",
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((response) => handleAddValue(response))
    .catch((error: any) => console.log(error));

  return (
    <div>
      <div>The Value is: {value}</div>
      <AddButon handleAddValue={handleAddValue} />
    </div>
  );
};

// import { FC, useState } from "react";
// interface IUsersProps {}

// export const Users: FC<IUsersProps> = (props) => {
//   const { user, setUser }: any = useState(0);
//   const responseHandler: any = (response: any) => {
//     if (response) {
//       console.log(response);
//       setUser(...user, response);
//     }
//   };
//   fetch(`http://localhost:5000/auth/get_users`, {
//     mode: "cors",
//     method: "GET",
//     headers: {
//       "Content-Type": "application/json",
//     },
//   })
//     .then((response) => response.json())
//     .then((response) => responseHandler(response))
//     .catch((error: any) => console.log(error));
//   console.log(user);
//   return <div>{/* {users.values.map((u) => <p>{u.email}</p>)} */}</div>;
// };
