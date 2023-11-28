import React from "react";
import logo from "../assets/images/logo.jpg";
import { Link } from "react-router-dom";

const Tabs = ({ tabs }) => {
  const smoothScrollTo = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };
  return (
    <div className="">
      <div className="flex flex-row pt-4">
        <img src={logo} alt="logo" className="h-12 w-10 pt-2"></img>
        <ul
          className="mb-4 flex flex-row list-none border-b-0 pl-0"
          role="tablist"
          data-te-nav-ref
        >
          {tabs.map((tab, index) => (
            <Link
              to={"/"}
              className={
                "block border-x-0 border-b-2 border-t-0 border-transparent px-7 pb-3.5 pt-4 text-md font-medium uppercase leading-tight text-neutral-300 hover:border-slate-500 hover:bg-brown-500"
              }
              id={tab.id}
              role="tab"
            >
              <li key={index} role="presentation">
                {tab.label}
              </li>
            </Link>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Tabs;
