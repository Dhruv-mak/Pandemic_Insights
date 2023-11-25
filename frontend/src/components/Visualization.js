import React from "react";
import Navbar2 from "./Navbar2";
import DropdownButton from "./DropdownButton";
import QueryNavBar from "./QueryNavBar";


export default function Visualization() {
  return (
    <div className="Visual">

      <div className="mb-8">
        <QueryNavBar />
      </div>
      

      <div>
        <Navbar2 />
      </div>

      <div className="flex justify-center mt-60">
        <DropdownButton />
      </div>
    </div>
  );
}
