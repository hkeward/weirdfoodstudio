import metadata from "../assets/metadata.json";

const load_database = ({ commit }) => {
  commit("SET_METADATA", metadata);
  var id_metadata = {};
  for (var category in metadata) {
    id_metadata[category] = {};
    for (var img_index in metadata[category]) {
      var img_obj = metadata[category][img_index];
      id_metadata[category][img_obj.id] = img_obj;
    }
  }
  commit("SET_ID_METADATA", id_metadata);
  commit("SET_CATEGORIES", metadata);
};

const get_set_nav_width = ({ state, commit }, set_width) => {
  var width;
  if (typeof set_width !== "undefined") {
    width = set_width;
  } else {
    if (state.menu_expanded) {
      width = state.nav_width_expanded;
    } else {
      width = state.nav_width_collapsed;
    }
  }

  commit("SET_NAVWIDTH", width);
};

const toggle_menu = ({ state, commit, dispatch }, mobile) => {
  var menu_was_expanded = state.menu_expanded;
  commit("TOGGLE_MENU", !menu_was_expanded);
  if (mobile === false) {
    dispatch("get_set_nav_width");
  }
};

const toggle_zoomed = ({ state, commit }) => {
  var was_zoomed = state.zoomed;
  commit("TOGGLE_ZOOMED", !was_zoomed);
};

export default {
  load_database,
  get_set_nav_width,
  toggle_menu,
  toggle_zoomed,
};
