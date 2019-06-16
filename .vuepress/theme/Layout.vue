<template>
	<article>
		<script src="https://kit.fontawesome.com/78be0865e8.js"></script>
		<header>
			<div class="vcard">
				<h1 class="fn">David H. Bronke</h1>
				<div class="n" style="display: none">
					Prefix: <span class="honorific-prefix">Mr.</span><br>
					First Name: <span class="given-name">David</span><br>
					Middle Name: <span class="additional-name">Henry</span><br>
					Last Name: <span class="family-name">Bronke</span>
				</div>
				<dl v-if="$site.themeConfig.showContactInfo" :class="{'alt-layout': Boolean($site.themeConfig.url)}">
					<dt class="email-label"><i class="far fa-envelope"></i></dt>
						<dd class="email">
							<a class="value" :href="'mailto:' + $site.themeConfig.email">{{ $site.themeConfig.email }}</a>
						</dd>

					<dt class="adr-label"><i class="fas fa-map-marker-alt"></i></dt>
						<dd class="adr-container">
							<!--a class="adr" :href="https://maps.apple.com/?q=' + $site.themeConfig.addressQuery"-->
							<div class="adr">
								<div class="street-address">{{ $site.themeConfig.address1 }}</div>
								<div v-if="$site.themeConfig.address2" class="extended-address">{{ $site.themeConfig.address2 }}</div>
								<div>
									<span class="locality">{{ $site.themeConfig.city }}</span>,
									<abbr class="region" :title="$site.themeConfig.state">{{ $site.themeConfig.stateAbbr }}</abbr>
									<span class="postal-code">{{ $site.themeConfig.zip }}</span>
								</div>
								<div class="country-name">{{ $site.themeConfig.country }}</div>
							</div>
						</dd>

					<dt v-if="$site.themeConfig.phoneNumber" class="tel-label"><i class="fas fa-phone"></i></dt>
						<dd v-if="$site.themeConfig.phoneNumber" class="tel">
							<abbr class="type" title="home"></abbr>
							<abbr class="type" title="voice"></abbr>
							<a class="value" :href="'tel:' + $site.themeConfig.phoneNumber">{{ $site.themeConfig.phoneNumber }}</a>
						</dd>

					<dt v-if="$site.themeConfig.url" class="url-label"><i class="fas fa-globe"></i></dt>
						<dd v-if="$site.themeConfig.url" class="url">
							<a class="value" :href="$site.themeConfig.url">{{ $site.themeConfig.url }}</a>
						</dd>
				</dl>
			</div>

			<nav>
				<a v-for="page in pages" :class="{current: $page.key == page.key}" :href="page.path">{{ page.title }}</a>
			</nav>
		</header>

		<section>
			<Content/>
		</section>
	</article>
</template>

<style>
@import url('https://fonts.googleapis.com/css?family=Raleway:400,300italic|Quattrocento+Sans:400,400italic,700,700italic|Oxygen+Mono');

* {
	box-sizing: border-box;
}

html {
	background: #121312;
	background-size: cover;
	color: #eeefee;
	text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.25);
}

body {
	margin: 0;
	padding: 0;
	font-family: 'Quattrocento Sans', sans-serif;
}

a:link, a:visited {
	color: #eeffee;
	text-decoration: underline #4f5;
}

a:hover, a:focus {
	color: #fff;
	text-decoration: underline #6f7;
}

a.header-anchor {
	float: right;
	font-size: 0.75rem;
}

h1, h2, h3, h4, h5 {
    font-family: 'Raleway', sans-serif;
    clear: both;
    border-bottom: 1px solid #eee;
    margin-bottom: 0.2em;
}
h1:first-child {
    margin-top: 0;
}

code, kbd, pre, samp {
    font-family: 'Oxygen Mono';
    font-size: 0.8em;
}

header:before {
	display: block;
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: -1;
	background: #121312 url('https://res.cloudinary.com/whitelynx/image/upload/v1560624377/DSC01579_kwokrv.jpg') no-repeat 50% 0;
	background-size: cover;
}

header {
	position: relative;
	margin: 0;
	padding: 1rem 1rem 0;
	z-index: 1;
	border-bottom: 1px solid black;
	box-shadow: 0 2px 7px rgba(0, 0, 0, 0.5);
	text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.65);
}

header .vcard > * {
	float: right;
}

header .vcard > h1 {
	float: left;
	margin-top: 0;
	padding: 0.25em 0;
	text-shadow: 1px 2px 4px rgba(0, 0, 0, 0.45);
}

header nav {
	clear: both;
	margin: 0 -1rem;
	padding: 0;
	display: grid;
	grid-template-columns: 1fr 1fr 1fr 1fr;
	grid-gap: 2px;
	text-align: center;
}

header nav a:link, header nav a:visited {
	display: block;
    flex: 0 1 auto;
    align-self: auto;
	margin: 0;
	padding: 0.5em 1em;
	color: #eee;
	background: rgba(0, 0, 0, 0.25);
	border-top: 2px solid transparent;
	border-bottom: 2px solid transparent;
	text-decoration: none;
}

header nav a:hover, header nav a:focus {
	color: #eee;
	background: rgba(0, 0, 0, 0.375);
	border-bottom-color: rgba(255, 255, 255, 0.25);
}

header nav a.current {
	color: #fff;
	background: rgba(0, 0, 0, 0.5);
	border-bottom-color: rgba(0, 255, 48, 0.5);
}

section {
	position: relative;
	margin: 0 0 2rem;
	padding: 1rem;
	background: rgba(40, 44, 40, 0.5);
}
header + section {
	border-top-left-radius: 0;
	border-top-right-radius: 0;
}

section > p:first-child,
section > .content__default > p:first-child {
	margin-top: 0;
}
section > p:last-child,
section > .content__default > p:last-child {
	margin-bottom: 0;
}

@media screen and (min-width: 680px) {
	header {
		padding: 10% 0 0;
	}
	header nav, header .vcard {
		width: 680px;
		margin: 0 auto;
	}

	header nav {
		display: flex;
		flex-direction: row;
		flex-wrap: nowrap;
		justify-content: flex-start;
		align-content: flex-start;
		align-items: flex-end;
	}
	header nav a:link, header nav a:visited {
		margin: 0 0 0 1em;
	}

	section {
		margin: 0 auto 2rem;
		width: 680px;
		box-shadow: 1px 3px 6px rgba(0, 0, 0, 0.35);
		border-radius: 4px;
	}
}

@media screen and (min-width: 1133px) {
	header {
		padding: 10% 20% 0;
	}
	header nav, header .vcard {
		width: auto;
		margin: 0;
	}

	section {
		margin: 0 20% 2rem;
		width: auto;
	}
}

.grid {
	display: grid;
	grid-template-columns: 1fr 1fr 1fr;
	grid-gap: 1rem;
}
.grid > a {
	background: rgba(0, 0, 0, 0.5);
	border-radius: 8px;
	text-align: center;
	padding: 2em 0;
	text-decoration: none;
	transition: all 300ms ease-in-out;
}
.grid > a > i, .grid > a > svg {
	display: block;
	fill: #fff;
	font-size: 5em;
	width: 80px;
	text-decoration: none;
	margin: 0 auto 1rem;
	transition: all 300ms ease-in-out;
}
.grid > a:hover, .grid > a:focus {
	background: #000;
}
.grid > a:hover > i.fa-gitlab, .grid > a:focus > i.fa-gitlab {
	color: #e65328;
}
.grid > a:hover > i.fa-linkedin, .grid > a:focus > i.fa-linkedin {
	color: #0073b1;
}


dl {
	margin-top: 0;
	margin-bottom: 0;
}
dt {
	position: relative;
	width: 25%;
	float: left;
	clear: both;
	margin: 0.7em 0 0;
	color: #080;
	font-weight: bold;
	text-align: right;
	page-break-inside: avoid;
}
dt a[href] {
	color: #080;
	text-decoration-line: underline;
	text-decoration-color: #46c146;
}
dt a[href]:hover,
dt a[href]:focus {
	text-decoration-color: #080;
}
dt em {
	display: block;
	font-weight: normal;
	font-size: 8pt;
	color: #17a417;
}
dt + dd {
	margin: 0.7em 0 0;
}
dt:last-of-type {
	margin-bottom: 0.9em;
}
dt svg {
	margin-right: 0.2ex;
}
dd {
	float: right;
	clear: right;
	padding: 0 0 0.25em 1em;
	width: 75%;
	margin: 0;
	page-break-inside: avoid;
}
dd:last-child {
	margin-bottom: 0.9em;
}
dd em {
	font-size: 11pt;
}

h1:first-child {
	margin-top: 0;
}
.vcard {
	page-break-inside: avoid;
	position: relative;
}
.vcard dl {
	display: grid;
	grid-template-columns: 55px 1fr;
	margin-bottom: 0.6em;
}
.vcard dl.alt-layout {
	grid-template-areas: "dt1 dd1" "dt2 dd2" "dt3 dd3" "dt4 dd4";
}
.vcard dl.alt-layout dt.email-label {
	grid-area: dt1;
}
.vcard dl.alt-layout dd.email {
	grid-area: dd1;
}
.vcard dl.alt-layout dt.tel-label {
	grid-area: dt2;
}
.vcard dl.alt-layout dd.tel {
	grid-area: dd2;
}
.vcard dl.alt-layout dt.url-label {
	grid-area: dt3;
}
.vcard dl.alt-layout dd.url {
	grid-area: dd3;
}
.vcard dl.alt-layout dt.adr-label {
	grid-area: dt4;
}
.vcard dl.alt-layout dd.adr-container {
	grid-area: dd4;
}
.vcard dl dt,
.vcard dl dd {
	width: auto;
	margin-bottom: 0;
}
.vcard + h2 {
	margin-top: 0;
}
@media screen and (min-width: 680px) {
	.vcard dl {
		display: grid;
		grid-template-columns: 25px 1fr repeat(2, 55px 1fr);
		margin-bottom: 0.6em;
	}
	.vcard dl.alt-layout {
		grid-template-columns: 25px 4fr 55px 3fr;
		grid-template-rows: repeat(3, 1fr);
		grid-template-areas: "dt1 dd1 dt4 dd4" "dt2 dd2 dt4 dd4" "dt3 dd3 dt4 dd4";
	}
}
@media print {
	.vcard {
		position: relative;
		border-bottom: 1px solid #eee;
	}
	.vcard::before {
		position: absolute;
		top: 0;
		right: 0;
		color: #f8f8f8;
		content: 'Résumé';
		font-weight: bold;
		font-style: italic;
		font-size: x-large;
	}
	.vcard dl {
		display: grid;
		grid-template-columns: repeat(3, 55px 1fr);
		margin-bottom: 0.6em;
	}
	.vcard dl.alt-layout {
		grid-template-columns: 55px 3fr 55px 2fr;
		grid-template-rows: repeat(3, 1fr);
		grid-template-areas: "dt1 dd1 dt4 dd4" "dt2 dd2 dt4 dd4" "dt3 dd3 dt4 dd4";
	}
	.vcard dl.alt-layout dt.email-label {
		grid-area: dt1;
	}
	.vcard dl.alt-layout dd.email {
		grid-area: dd1;
	}
	.vcard dl.alt-layout dt.tel-label {
		grid-area: dt2;
	}
	.vcard dl.alt-layout dd.tel {
		grid-area: dd2;
	}
	.vcard dl.alt-layout dt.url-label {
		grid-area: dt3;
	}
	.vcard dl.alt-layout dd.url {
		grid-area: dd3;
	}
	.vcard dl.alt-layout dt.adr-label {
		grid-area: dt4;
	}
	.vcard dl.alt-layout dd.adr-container {
		grid-area: dd4;
	}
	.vcard dl dt,
	.vcard dl dd {
		width: auto;
		margin-bottom: 0;
	}
	.vcard + h2 {
		margin-top: 0;
	}
}
</style>

<script>
import * as _ from "lodash";

export default {
	computed: {
		pages: function () {
			return _.orderBy(this.$site.pages, page => page.frontmatter.order);
		}
	}
}
</script>
