/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [
		'./src/*.html',
	],
	theme: {
		screens: {
			lg: { 'max': '1999.99px' },
			md: { 'max': '991.99px' },
			sm: { 'max': '767.99px' },
			xs: { 'max': '479.99px' },
		},
		extend: {
			backgroundImage: {
			},
			fontFamily: {
				WorkSans: ['Work Sans', 'sans-serif'],
				Merriweather: ['Merriweather', 'sans-serif']
			},
			colors: {
				bluee: '#2563EB',
			}
		},
	},
	plugins: [],
}

