import sublime

html_svelte = [
	sublime.CompletionItem(
		"if",
		annotation="if",
		completion="{#if true}\n\t\n{/if}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"elif",
		annotation="else if",
		completion="{:else if false}\n\t\n{:else}\n\t",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"each",
		annotation="each",
		completion="{#each items as item, i}\n\t\n{/each}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"await",
		annotation="await",
		completion="{#await promise}\n\t\n{:then value}\n\t\n{:catch error}\n\t\n{/await}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"key",
		annotation="key",
		completion="{#key value}\n\t\n{/key}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"html",
		annotation="html",
		completion="{@html post.content}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"debug",
		annotation="debug",
		completion="{@debug data}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"const",
		annotation="const",
		completion="{@const value = 1+1}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"bind",
		annotation="bind:value",
		completion="bind:value={name}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"bind",
		annotation="bind:files",
		completion="bind:files={name}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"bind",
		annotation="bind:group",
		completion="bind:group={variable}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"bind",
		annotation="bind:innerHTML",
		completion="bind:innerHTML={html}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"bind",
		annotation="bind:this",
		completion="bind:this={variable}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"bind",
		annotation="bind:open",
		completion="bind:open={isOpen}",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"transition",
		annotation="transition:fade",
		completion="transition:fade=\"{{ duration: 2000 }}\"",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:self",
		completion="<svelte:self count=\"{count - 1}\"/>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:component",
		completion="<svelte:component this={value.component}/>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:element",
		completion="<svelte:element this={tag}>\n\t\n</svelte:element>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:window",
		completion="<svelte:window/>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:body",
		completion="<svelte:body/>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:head",
		completion="<svelte:head>\n\t\n</svelte:head>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:options",
		completion="<svelte:options tag=\"my-custom-element\"/>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"svelte",
		annotation="svelte:fragment",
		completion="<svelte:fragment slot=\"name\">\n\t\n</svelte:fragment>",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]

js_svelte = [
	sublime.CompletionItem(
		"on",
		annotation="onMount",
		completion="onMount(() => {\n\treturn () => {}\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"on",
		annotation="beforeUpdate",
		completion="beforeUpdate(() => {\n\t\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"on",
		annotation="afterUpdate",
		completion="afterUpdate(() => {\n\t\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"on",
		annotation="onDestroy",
		completion="onDestroy(() => {\n\t\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"context",
		annotation="setContext",
		completion="setContext('name', 1);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"context",
		annotation="getContext",
		completion="const name = getContext('name');",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"context",
		annotation="hasContext",
		completion="hasContext('name')",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"context",
		annotation="getAllContexts",
		completion="const contexts = getAllContexts();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"event",
		annotation="createEventDispatcher",
		completion="const dispatch = createEventDispatcher();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"store",
		annotation="subscribe",
		completion="const unsubscribe = data.subscribe(value => {\n\tconsole.log(value);\n});",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"store",
		annotation="derived",
		completion="const data = derived(a, $a => $a * 2);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"store",
		annotation="get",
		completion="const value = get(store);",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte",
		completion="import {\n\tonMount, beforeUpdate, afterUpdate, onDestroy, tick\n\tsetContext, getContext, hasContext, getAllContexts, createEventDispatcher\n} from 'svelte';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte/store",
		completion="import { writable, readable, derived, get } from 'svelte/store';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte-navigator",
		completion="import {\n\tRouter, Link, Route, link,\n\tuseNavigate, useLocation, useResolve, useResolvable, useMatch, useParams, useFocus\n} from 'svelte-navigator';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte/motion",
		completion="import { tweened, spring } from 'svelte/motion';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte/easing",
		completion="import {  } from 'svelte/easing';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte/transition",
		completion="import { fade, blur, fly, slide, scale, draw, crossfade } from 'svelte/transition';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"import",
		annotation="svelte/animate",
		completion="import { flip } from 'svelte/animate';",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use",
		annotation="useNavigate",
		completion="const navigate = useNavigate();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use",
		annotation="useLocation",
		completion="const location = useLocation();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use",
		annotation="useResolve",
		completion="const resolve = useResolve();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use",
		annotation="useResolvable",
		completion="const resolvedLink = useResolvable(\"relativePath\");",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use",
		annotation="useParams",
		completion="const params = useParams();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
	sublime.CompletionItem(
		"use",
		annotation="useFocus",
		completion="const focus = useFocus();",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET
	),
]

non_svelte = [
	sublime.CompletionItem(
		"store",
		annotation="writable",
		completion="import { writable } from 'svelte/store';\n\nconst data = writable(0);\n\nexport default data;",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET,
		details='create writable and export it'
	),
	sublime.CompletionItem(
		"store",
		annotation="readable",
		completion="import { readable } from 'svelte/store';\n\nconst data = readable(0, set => {\n\tset(1);\n});\n\nexport default data;",
		completion_format=sublime.COMPLETION_FORMAT_SNIPPET,
		kind=sublime.KIND_SNIPPET,
		details='create readable and export it'
	),
]