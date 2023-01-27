import React, { useContext } from "react";
import { BrowserRouter, Link, useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const Header = ({ title }) => {
  const [token, setToken] = useContext(UserContext);
  const [nickname, setNickname] = useContext(UserContext);
  const [id, setId] = useContext(UserContext);
  const [email, setEmail] = useContext(UserContext);

  const handleLogout = () => {
    setToken(null);
    setNickname(null);
    setId(null);
    setEmail(null);
  };

  return (
    <div className="has-text-centered m-6">
      <BrowserRouter>
        <Link to="/" className="title">
          <h1
            onClick={() => {
              window.location.href = "/";
            }}
          >
            {title}
          </h1>
        </Link>
      </BrowserRouter>

      {token && (
        <button className="button" onClick={handleLogout}>
          Logout
        </button>
      )}
    </div>
  );
};

export default Header;
