import React from "react";

const Card = ({ img_src, title}) => {
  return (
    <div className="relative max-w-xl mx-auto mt-20">
      <img
        className="h-72 w-full object-cover rounded-md"
        alt="card"
        src={img_src}
      />
      <div className="absolute inset-0 bg-gray-700 opacity-60 rounded-md"></div>
      <div className="absolute inset-0 flex items-center justify-end flex-col">
        <h2 className="text-white text-3xl font-bold">{title}</h2>
        <button
          type="button"
          className="my-7 inline-block rounded border-2 border-primary-100 px-6 pb-[6px] pt-2 text-xs font-medium uppercase leading-normal text-primary-700 transition duration-150 ease-in-out hover:border-brown-500 hover:bg-neutral-500 hover:bg-opacity-20 focus:border-primary-accent-100 focus:outline-none focus:ring-0 active:border-primary-accent-200 font-bold"
          data-te-ripple-init 
        >
          <b>Get Queries</b>
        </button>
      </div>
    </div>
  );
};
export default Card;
