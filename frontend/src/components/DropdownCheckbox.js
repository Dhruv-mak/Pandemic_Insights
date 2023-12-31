import React, { useState } from "react";

const DropdownCheckbox = ({ buttonText, checkboxItems, handleCheck }) => {
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setIsDropdownOpen(!isDropdownOpen);
  };

  return (
    <div className="relative inline-block text-left">
      {/* Button */}
      <button
        id="dropdownCheckboxButton"
        onClick={toggleDropdown}
        className="text-white bg-slate-800/80 hover:bg-slate-800/90 focus:ring-4 focus:outline-none focus:ring-slate-800/95 font-medium rounded-lg text-sm px-5 py-2.5 text-center inline-flex items-center"
        type="button"
      >
        {buttonText}{" "}
        <svg
          className={`w-2.5 h-2.5 ms-3 transition-transform ${
            isDropdownOpen ? "rotate-180" : ""
          }`}
          aria-hidden="true"
          xmlns="http://www.w3.org/2000/svg"
          fill="none"
          viewBox="0 0 10 6"
        >
          <path
            stroke="currentColor"
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="m1 1 4 4 4-4"
          />
        </svg>
      </button>

      {/* Dropdown menu */}
      <div
        id="dropdownDefaultCheckbox"
        className={`${
          isDropdownOpen ? "block" : "hidden"
        } z-10 absolute left-0 mt-2 w-48 max-h-60 overflow-y-auto bg-white divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 dark:divide-gray-600`}
      >
        <ul className="p-3 space-y-3 text-sm text-gray-700 dark:text-gray-200">
          {checkboxItems.map((item, index) => (
            <li key={index}>
              <div className="flex items-center">
                <input
                  id={item.id}
                  type="checkbox"
                  value=""
                  className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-700 dark:focus:ring-offset-gray-700 focus:ring-2 dark:bg-gray-600 dark:border-gray-500"
                  defaultChecked={item.checked}
                  onChange={() => handleCheck(item.id)}
                />
                <label
                  htmlFor={item.id}
                  className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                >
                  {item.label}
                </label>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default DropdownCheckbox;