import React from "react";
import Card from "./Card";
import doctorImage from "../assets/images/doctors.jpg";
import epidemiologistImage from "../assets/images/epidemiologists.jpg";
import policyMakerImage from "../assets/images/policy_makers.jpg";
import generalPublicImage from "../assets/images/general_public.jpg";
import environmentalScientistImage from "../assets/images/environmentalScientistImage.jpg";
import {Link} from "react-router-dom";
const Users = ({ users }) => {
  return (
    <div
      id="users"
      className="bg-[#c8becc] bg-gradient-to-br from-[#a26e25] via-[#ffffff] to-[#0c555c] pb-12  flex justify-center items-center"
    >
      <div className="flex flex-row flex-wrap gap-10 justify-center">
        <Link to="/Doctors"><Card title="Doctors" img_src={doctorImage}></Card></Link>
        <Link to="/Epidemiologists"><Card title="Epidemiologists" img_src={epidemiologistImage}></Card></Link>
        <Link to="/Policy Makers"><Card title="Policy Makers" img_src={policyMakerImage}></Card></Link>
        <Link to="/General Public"><Card title="General Public" img_src={generalPublicImage}></Card></Link>
        <Link to="/Environmental Scientists"><Card title="Environmental Scientists" img_src={environmentalScientistImage}></Card></Link>
        

      </div>
    </div>
  );
};
export default Users;
