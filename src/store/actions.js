import metadata from "../assets/metadata.json";

const load_database = ({ commit }) => {
  commit("SET_METADATA", metadata);
  commit("SET_CATEGORIES", metadata);
};

const get_set_nav_width = ({ state, commit }) => {
  var width;
  if (state.menu_expanded) {
    width = state.nav_width_expanded;
  } else {
    width = state.nav_width_collapsed;
  }

  commit("SET_NAVWIDTH", width);
};

const toggle_menu = ({ state, commit, dispatch }) => {
  var menu_was_expanded = state.menu_expanded;
  commit("TOGGLE_MENU", !menu_was_expanded);
  dispatch("get_set_nav_width");
};

export default {
  load_database,
  get_set_nav_width,
  toggle_menu,
};
