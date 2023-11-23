import React from "react";
import Card from "./Card";
import doctorImage from "../assets/images/doctor.jpg";
const Users = ({ users }) => {
  return (
    <div id="users" className="bg-[#c8becc] bg-gradient-to-br from-[#cac7e9] via-[#b7b7e0] to-[#cbacec] h-screen pt-20">
      <div className="flex flex-row flex-wrap gap-10 px-36 justify-center">
        <Card
          title="Doctors"
          img_src={doctorImage}
        ></Card>
        <Card
          title="Epidemiologists"
          img_src={doctorImage}
        ></Card>
        <Card
          title="Policy Makers"
          img_src={doctorImage}
        ></Card>
        <Card
          title="General Public"
          img_src={doctorImage}
        ></Card>
      </div>
    </div>
  );
};
export default Users;
