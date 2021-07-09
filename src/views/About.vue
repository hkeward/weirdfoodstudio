<template>
  <div id="about">
    <div id="img_socials">
      <div class="artist_image">
        <img v-bind:src="getArtistImgUrl()" />
      </div>
      <div class="socials">
        <a href="https://www.instagram.com/weird_food_studio/">
          <font-awesome-icon
            v-bind:icon="['fab', 'instagram']"
          ></font-awesome-icon>
        </a>
      </div>
    </div>
    <div id="description">
      <p>
        <strong>Jessi Wood</strong> illustrates, prints, paints, draws, and
        generally toys with wistful forces within the Weird Food Studio that
        cannot be understood
      </p>
      <br />
      <p>And tits.</p>
      <p>Lots of tits, I tell yah</p>
      <br />
      <p>
        A lady who summons powers of the weird, the grimy, the melancholic, and
        the deep, electric pull you feel towards a juicy fruit you can’t have,
        before noticing it’s growing a vulva
      </p>
      <br />
      <p>
        Harnessing those vibes, she crafts visual bubblegum for surrounding
        eyeballs to chew
      </p>
      <br />
      <p>
        Similar, strange folk are welcome to join her in collaboration or
        commission
      </p>
      <br />
      <p>
        Find more of her weird food on
        <a href="https://www.instagram.com/weird_food_studio/">Instagram</a>,
        find her prints on Etsy, and find her below the cherry moon in an
        ancient dusk
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  methods: {
    getArtistImgUrl() {
      return require("../assets/jessi_about_me.jpg");
    },
  },
};
</script>

<style scoped>
#about {
  text-align: left;
  font-size: 2em;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
}
img {
  max-width: 100%;
  border-radius: 7px;
}
#img_socials {
  display: flex;
  flex-direction: column;
  flex-basis: 40%;
  margin-right: 30px;
}
#description {
  flex-basis: 60%;
}
.socials {
  font-size: 2em;
  align-self: center;
}

@media screen and (max-width: 990px) {
  #about {
    width: 100%;
    flex-wrap: wrap;
  }
  #img_socials {
    flex-basis: 100%;
    margin-bottom: 10px;
  }
  #description {
    flex-basis: 100%;
    align-items: center;
  }
}
</style>
