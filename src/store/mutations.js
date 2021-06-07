const SET_METADATA = (state, metadata) => {
  state.metadata = metadata;
};

const SET_CATEGORIES = (state, metadata) => {
  state.categories = Object.keys(metadata);
};

export default {
  SET_METADATA,
  SET_CATEGORIES,
};
