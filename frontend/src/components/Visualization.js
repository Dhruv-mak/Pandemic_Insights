import React from "react";
import Navbar2 from "./Navbar2";
import DropdownButton from "./DropdownButton";

export default function Visualization() {
  return (
    <div className="Visual">
      <div>
        <Navbar2 />
      </div>

      <div className="flex justify-center mt-60">
        <DropdownButton />
      </div>

      <div className="flex justify-center mt-60 text-6xl text-gray-900 dark:text-red">
        Schneider Shock!!! Sakshi Rock!!!
      </div>
    </div>
  );
}