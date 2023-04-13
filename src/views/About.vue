<template>
  <div id="about">
    <div id="img_socials">
      <div class="artist_image">
        <img v-bind:src="getArtistImgUrl()" />
      </div>
      <div class="socials">
        <a href="https://patreon.com/weirdfoodstudio">
          <font-awesome-icon
            v-bind:icon="['fab', 'patreon']"
          ></font-awesome-icon>
        </a>
      </div>
    </div>
    <div id="description">
      <h2 id="about_me_header">Art is like food</h2>
      <h3 id="about_me_subheader">It sticks to your insides</h3>
      <p>I make:</p>
      <ul>
        <li>
          <strong>Commission work on-demand</strong> (editorial illustrations,
          portraits, album covers, etc.)
        </li>
        <li><strong>Original work</strong></li>
        <li><strong>Prints of original work</strong></li>
        <li>
          <strong>Lino prints</strong> (physically designed, hand carved–no
          computer involved)
        </li>
        <li><strong>Comics</strong> (coming soon...)</li>
      </ul>
      <p>
        I use multiple mediums, including lino printing, acrylic, watercolour,
        collage, digital tools (Adobe Illustrator and Photoshop), ink, and
        pencil.
      </p>
      <p>
        My specialty is surreal, uncanny imagery rendered in a comic-like style,
        but I’m flexible.
      </p>
      <p>
        I studied formally at OCAD University (Toronto, Ontario) before
        relocating to work in Waterloo.
      </p>
      <p>I’m a versatile emerging artist, looking for her next meal.</p>
      <p id="signoff">Eat Weird,</p>
      <p id="signature">-Jessi, Canadian illustrator and printmaker</p>
      <p>
        Contact artist for commissions and collaborations here:
        <strong
          ><a href="mailto:weirdfoodstudio@gmail.com"
            >weirdfoodstudio@gmail.com</a
          ></strong
        >
      </p>
      <h2>Support the artist here:</h2>
      <ul>
        <li>
          <a href="https://patreon.com/weirdfoodstudio" class="social_link"
            >Patreon</a
          >
        </li>
      </ul>
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
#about_me_header {
  margin: 0px;
}

#about_me_subheader {
  margin: 0px 5px 50px 0px;
}

#signoff {
  margin: 50px 50px 5px 0px;
}

#signature {
  margin: 0px 0px 50px 15px;
}

#about {
  text-align: left;
  font-size: 120%;
  display: flex;
  flex-direction: row;
  flex-wrap: nowrap;
  margin: 15px 0px 0px 0px;
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
  font-size: 200%;
  align-self: center;
  width: 100%;
  display: flex;
  justify-content: space-around;
  gap: 20px;
}

.social_link {
  text-decoration: underline;
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
