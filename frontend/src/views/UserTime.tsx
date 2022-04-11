import React, { useState, useEffect } from 'react';

function UserTime() {
  const [currentTime, setCurrentTime] = useState(0);
  const [currentUser, setCurrentUser] = useState(0);

  useEffect(() => {
    fetch('/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
      setCurrentUser(data.user)
    });
  }, []);


  return (
    <div>
        <p>The current time is {currentTime}.</p>
        <p>The current user is {currentUser}</p>
    </div>
  );
}

export default UserTime;
