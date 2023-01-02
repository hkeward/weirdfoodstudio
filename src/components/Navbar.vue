<template>
  <div>
    <div v-if="menu_expanded" id="nav" :style="navbarStyle">
      <div @click="toggle_menu(mobile)" :id="nav_close">
        <font-awesome-icon icon="times-circle"></font-awesome-icon>
      </div>
      <div id="links-wrapper" class="links">
        <div id="links-top" class="links">
          <router-link
            to="/collage"
            @click="scrollClose"
            :class="{ 'is-active': subIsActive('/collage') }"
            >Collage</router-link
          >
          <router-link
            to="/lino"
            @click="scrollClose"
            :class="{ 'is-active': subIsActive('/lino') }"
            >Lino</router-link
          >
          <p id="illustrations_section">Illustrations</p>
          <ul id="illustration_types">
            <li>
              <router-link
                to="/illustrations-digital"
                @click="scrollClose"
                :class="{ 'is-active': subIsActive('/illustrations-digital') }"
                >Digital</router-link
              >
            </li>
            <li>
              <router-link
                to="/illustrations-physical"
                @click="scrollClose"
                :class="{ 'is-active': subIsActive('/illustrations-physical') }"
                >Physical</router-link
              >
            </li>
          </ul>
          <router-link
            v-if="'comics' in metadata"
            to="/comics"
            @click="scrollClose"
            :class="{ 'is-active': subIsActive('/comics') }"
            >Comics</router-link
          >
        </div>
        <div id="links-bottom" class="links">
          <a href="https://weirdfoodstudio.etsy.com">Shop</a>
          <router-link to="/contact" @click="scrollClose">Contact</router-link>
          <router-link to="/" @click="scrollClose">Home</router-link>
        </div>
      </div>
    </div>
    <div v-else id="nav" :style="navbarStyle">
      <div @click="toggle_menu(mobile)">
        <font-awesome-icon icon="hamburger"></font-awesome-icon>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  name: "Navbar",
  props: {
    mobile: Boolean,
  },
  computed: {
    ...mapState(["menu_expanded", "metadata"]),
    navbarStyle() {
      if (this.mobile === true) {
        if (this.menu_expanded === true) {
          return {
            width: "100%",
            top: 0,
            left: 0,
            margin: 0,
            padding: "20px 0 0 0",
            "border-radius": 0,
            "text-align": "center",
            "max-height": "unset",
          };
        } else {
          return {
            height: "auto",
            margin: 0,
            padding: "10px",
          };
        }
      } else {
        return {};
      }
    },
    nav_close() {
      if (this.mobile === true) {
        return "nav_close_mobile";
      } else {
        return "nav_close";
      }
    },
  },
  methods: {
    ...mapActions(["get_set_nav_width", "toggle_menu"]),
    scrollClose() {
      window.scrollTo(0, 0);
      if (this.mobile === true) {
        this.toggle_menu();
      }
    },
    subIsActive(input) {
      const paths = Array.isArray(input) ? input : [input];

      return paths.some((path) => {
        return this.$route.path.indexOf(path) === 0; // current path starts with this path string
      });
    },
    handleEscape(event) {
      if (event.keyCode === 27) {
        if (this.mobile && this.menu_expanded) {
          this.toggle_menu();
        }
      }
    },
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener("keyup", (event) => this.handleEscape(event));
    });
  },
  beforeUnmount() {
    window.removeEventListener("keyup", (event) => this.handleEscape(event));
  },
};
</script>

<style scoped>
#illustrations_section {
  margin: 0;
  padding: 15px 0px 0px 0px;
}

#illustration_types {
  margin: 0;
  font-size: 80%;
  list-style-type: none;
  padding: 0 0 0 20px;
}

li {
  padding: 0;
  margin: 15px 0;
}

#nav {
  display: flex;
  flex-direction: column;
  position: fixed;
  height: 100%;
  max-height: 100vh;
  overflow-y: auto;
  text-align: left;
  padding: 50px;
  background-color: #82ced9;
  margin-left: 20px;
  border-radius: 7px;
  font-size: 225%;
  color: white;
  font-weight: 900;
}

#nav_close {
  text-align: center;
}

#nav_close_mobile {
  text-align: end;
  padding-right: 20px;
}

.links {
  display: flex;
  flex-direction: column;
}

#links-wrapper {
  justify-content: space-between;
  flex-basis: 90%;
}

#links-bottom {
  padding-bottom: 50px;
}

a {
  padding: 15px 0px;
}

a.router-link-exact-active,
.is-active {
  color: #001d91;
}
</style>
