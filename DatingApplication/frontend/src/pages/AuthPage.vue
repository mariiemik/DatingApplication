<template>
  <h1>Авторизация</h1>
  <div class="form-container">
    <form>
      <label for="email">EMAIL:</label>
      <input type="text" id="email" name="email" required>
      <br>
      <label for="password">PASSWORD:</label>
      <input type="password" id="password" name="password" required>
      <br>
      <button>
        <q-btn outline rounded color="primary" label="Outline Rounded"/> Войти
      </button>
  </form>
  </div>
</template>

<script>
export default {
  name: "auth",
  data() {
    return { email: "", password: ""};
  },
  methods: {
    async login() {
      const { email, password} = this;
      const res = await fetch(
        "https://SomberHandsomePhysics--five-nine.repl.co/register",
        { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ email, password }) }
      );
      const data = await res.json();
      console.log(data);
    }
  }
};
</script>

<style>
  body {
    background-color: darksalmon;    
  }
  h1 {
    font-weight: bold;
    text-align: center;
    color: whitesmoke;
  }
  .form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 50vh;
  }
  form {
    font-weight: bold;
    width:500px;
    height:160px;
    margin:auto;
    position:absolute;
    border: 4px inset lightpink;
    border-radius: 20px;
    padding: 20px;
  }
  input {
    width: 500px;
    height: 40px;
  }
  button {
    background-color: lemonchiffon;
    width: 90px;
    height: 25px;
    font-size: 15px;
    margin-top: 7px;
  }
  label {
    color: whitesmoke;
  }
</style>
