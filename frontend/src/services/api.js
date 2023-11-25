export async function get_query(index, country) {
  try {
    const response = await fetch(
      "http://localhost:5000/api/get_query/" + index + "/" + country
    );
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export async function get_coutry_list(index) {
  try {
    const response = await fetch("http://localhost:5000/api/get_countries/" + index);
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}

export async function dummy() {
  try {
    const response = await fetch("http://localhost:5000/api/dummy");
    if (!response.ok) {
      throw new Error("Network response was not ok");
    }
    const data = await response.json();
    return data;
  } catch (error) {
    console.error("Error fetching data:", error);
    throw error;
  }
}