import metadata from "../assets/metadata.json";

const load_database = ({ commit }) => {
  commit("SET_METADATA", metadata);
  commit("SET_CATEGORIES", metadata);
};

export default {
  load_database,
};
