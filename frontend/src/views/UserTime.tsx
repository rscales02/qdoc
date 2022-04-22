import React, { useState, useEffect } from "react";

function UserTime() {
  const [currentTime, setCurrentTime] = useState(0);
  const [currentUser, setCurrentUser] = useState(0);

  const savedToken = localStorage.getItem("user");
  useEffect(() => {
    const token = savedToken ? JSON.parse(savedToken) : { access_token: "" };
    console.log(token);
    fetch("/time", {
      headers: new Headers({
        HTTP_Authorization: "Bearer " + token["access_token"],
      }),
    })
      .then((res) => res.json())
      .then((data) => {
        setCurrentTime(data.time);
        setCurrentUser(data.user);
      });
  });

  return (
    <div>
      <p>The current time is {currentTime}.</p>
      <p>The current user is {currentUser}</p>
    </div>
  );
}

export default UserTime;
