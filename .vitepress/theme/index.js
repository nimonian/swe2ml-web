import { h } from 'vue'
import DefaultTheme from 'vitepress/theme'
import './style.css'

import Exercise from '../components/Exercise.vue'
import AnswerInput from '../components/AnswerInput.vue'
import vKatex from '../directives/katex'

/** @type {import('vitepress').Theme} */
export default {
  extends: DefaultTheme,
  Layout: () => {
    return h(DefaultTheme.Layout, null, {})
  },
  enhanceApp({ app, router, siteData }) {
    app.component('Exercise', Exercise)
    app.component('AnswerInput', AnswerInput)
    app.directive('katex', vKatex)
  }
}
