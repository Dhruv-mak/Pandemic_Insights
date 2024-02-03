const API_URL = "https://20.96.176.239/pandemic-insights";

export async function get_query(index, countryList, params = {}) {
  try {
    const url = new URL(`${API_URL}/get_query/${index}/${countryList}`);
    Object.keys(params).forEach(key => url.searchParams.append(key, params[key]));
    
    const response = await fetch(url);
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
    const response = await fetch(`${API_URL}/get_countries/${index}`);
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

export async function get_count() {
  try {
    const response = await fetch(`${API_URL}/get_count`);
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