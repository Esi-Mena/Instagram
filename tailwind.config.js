/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './Project/pixlpix/templates/**/*.html', //  templates are located here
    './project/static/**/*.js',      // static JavaScript files are located here
    // './src/**/*.{html,js}', // If you have a src folder with HTML and JS
    // Add other paths where Tailwind should look for classes
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin') //  installed flowbite
  ],
}

