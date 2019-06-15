<template>
	<article>
		<header>
			<div class="vcard">
				<h1 class="fn">David H. Bronke</h1>
				<div class="n" style="display: none">
					Prefix: <span class="honorific-prefix">Mr.</span><br>
					First Name: <span class="given-name">David</span><br>
					Middle Name: <span class="additional-name">Henry</span><br>
					Last Name: <span class="family-name">Bronke</span>
				</div>
				<dl :class="{'alt-layout': Boolean($site.themeConfig.url)}">
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
					<dt class="tel-label"><i class="fas fa-phone"></i></dt>
					<dd class="tel">
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
			<!--pre>{{ JSON.stringify($site, null, "  ") }}</pre>
			<pre>{{ JSON.stringify($page, null, "  ") }}</pre-->
		</section>
	</article>
</template>

<style>
html {
	background: #121312; /*url('https://res.cloudinary.com/whitelynx/image/upload/v1560618865/DSC02701_anjvlo.jpg') no-repeat 50% 0 fixed; */
	background-size: cover;
	color: #eeefee;
	text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.25);
}

body {
	margin: 0;
	padding: 0;
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


header:before {
	display: block;
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	width: 100%;
	height: 100%;
	z-index: -1;
	background: #121312 url('https://res.cloudinary.com/whitelynx/image/upload/v1560624377/DSC01579_kwokrv.jpg') no-repeat 0 0;
	background-size: cover;
}

header {
	position: relative;
	margin: 0;
	padding: 10% 20% 0;
	z-index: 1;
	border-bottom: 1px solid black;
	box-shadow: 0 2px 7px rgba(0, 0, 0, 0.5);
}

header .vcard > * {
	float: right;
}

header .vcard > h1 {
	float: left;
	margin-top: 0;
	padding: 0.25em 0;
	text-shadow: 1px 2px 4px rgba(0, 0, 0, 0.25);
}

header nav {
	clear: both;
	margin: 0;
	padding: 0;
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-content: flex-start;
    align-content: flex-start;
    align-items: flex-end;
}

header nav a:link, header nav a:visited {
	display: block;
    flex: 0 1 auto;
    align-self: auto;
	margin: 0 0 0 1em;
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
	margin: 0 20% 2rem;
	padding: 1rem;
	background: rgba(40, 44, 40, 0.5);
	box-shadow: 1px 3px 6px rgba(0, 0, 0, 0.35);
	border-radius: 4px;
}
header + section {
	border-radius: 0 0 4px 4px;
}

section > p:first-child {
	margin-top: 0;
}
section > p:last-child {
	margin-bottom: 0;
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
