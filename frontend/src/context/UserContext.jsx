import React, { createContext, useEffect, useState } from "react";

export const UserContext = createContext();

export const UserProvider = (props) => {
  const [token, setToken] = useState(localStorage.getItem("awesomeKanjiToken"));

  useEffect(() => {
    const fetchUser = async () => {
      const requestOptions = {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: "Bearer " + token,
        },
      };

      const response = await fetch("/api/users/me", requestOptions);
      const userdata = await response.json();
      if (!response.ok) {
        setToken(null);
      }
      localStorage.setItem("awesomeKanjiToken", token);
      localStorage.setItem("nickname", userdata.nickname);
      localStorage.setItem("id", userdata.id);
      localStorage.setItem("email", userdata.email);
    };
    fetchUser();
  }, [token]);

  return (
    <UserContext.Provider value={[token, setToken]}>
      {props.children}
    </UserContext.Provider>
  );
};
