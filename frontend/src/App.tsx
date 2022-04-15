import React from "react";
import "./App.css";
import { Routes, Route, Link } from "react-router-dom";
import { AppBar, IconButton, Toolbar, Typography } from "@mui/material";
import { Register } from "./views/Register";
import { Login } from "./views/Login";
import UserTime from "./views/UserTime";
import { Users } from "./views/Users";

function App() {
  return (
    <div className="App">
      <AppBar position="static">
        <Toolbar variant="dense">
          <IconButton
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          ></IconButton>
          <Typography variant="h6" color="inherit" component="div">
            <Link to="/auth/register">Register</Link>
            <Link to="/auth/login">Login</Link>
            <Link to="/time">Time</Link>
          </Typography>
        </Toolbar>
      </AppBar>
      <Routes>
        <Route path="/auth/register" element={<Register />} />
        <Route path="/auth/login" element={<Login />} />
        <Route path="/time" element={<UserTime />} />
        <Route path="/" element={<UserTime />} />
        <Route path="/auth/get_users" element={<Users />} />
      </Routes>
    </div>
  );
}

export default App;
