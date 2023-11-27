import React from "react";
import Card from "./Card";
import doctorImage from "../assets/images/doctor.jpg";
import {Link} from "react-router-dom";
const Users = ({ users }) => {
  return (
    <div
      id="users"
      className="bg-[#c8becc] bg-gradient-to-br from-[#a26e25] via-[#ffffff] to-[#0c555c] pb-12"
    >
      <div className="flex flex-row flex-wrap gap-10 px-36 justify-center">
        <Link to="/Doctors"><Card title="Doctors" img_src={doctorImage}></Card></Link>
        <Link to="/Epidemiologists"><Card title="Epidemiologists" img_src={doctorImage}></Card></Link>
        <Link to="/Policy Makers"><Card title="Policy Makers" img_src={doctorImage}></Card></Link>
        <Link to="/General Public"><Card title="General Public" img_src={doctorImage}></Card></Link>

      </div>
    </div>
  );
};
export default Users;
