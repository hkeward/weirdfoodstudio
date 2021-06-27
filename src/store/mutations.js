const SET_METADATA = (state, metadata) => {
  state.metadata = metadata;
};

const SET_ID_METADATA = (state, metadata) => {
  state.id_metadata = metadata;
};

const SET_CATEGORIES = (state, metadata) => {
  state.categories = Object.keys(metadata);
};

const SET_NAVWIDTH = (state, width) => {
  state.nav_width = width;
};

const TOGGLE_MENU = (state, menu_expanded) => {
  state.menu_expanded = menu_expanded;
};

export default {
  SET_METADATA,
  SET_ID_METADATA,
  SET_CATEGORIES,
  SET_NAVWIDTH,
  TOGGLE_MENU,
};
