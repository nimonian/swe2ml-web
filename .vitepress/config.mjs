import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Hck4ML',
  description: "The Hacker's guide to math for machine learning",
  srcDir: 'src',

  vite: {
    server: {
      port: process.env.VITE_PORT,
      strictPort: true,
      host: true,
      open: true
    }
  },

  markdown: {
    math: true,
    lineBreaks: true
  },

  themeConfig: {
    editLink: {
      pattern: 'https://github.com/nimonian/swe2ml-web/edit/main/src/:path'
    },

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Learn', link: '/learn' }
    ],

    sidebar: [
      {
        text: 'Vectors',
        collapsed: true,
        items: [
          {
            text: 'Components',
            link: '/learn/vectors/components'
          },
          {
            text: 'Dimensions',
            link: '/learn/vectors/dimensions'
          },
          {
            text: 'Adding vectors',
            link: '/learn/vectors/adding-vectors'
          },
          {
            text: 'Scaling vectors',
            link: '/learn/vectors/scaling-vectors'
          },
          {
            text: 'Vector magnitude',
            link: '/learn/vectors/vector-magnitude'
          },
          {
            text: 'Subtracting vectors',
            link: '/learn/vectors/subtracting-vectors'
          },
          {
            text: 'Unit vectors',
            link: '/learn/vectors/unit-vectors'
          },
          {
            text: 'Hadamard product',
            link: '/learn/vectors/hadamard-product'
          },
          {
            text: 'Dot product',
            link: '/learn/vectors/dot-product',
            items: [
              {
                text: 'Component formula',
                link: '/learn/vectors/dot-prod-formula'
              },
              {
                text: 'Magnitude revisited',
                link: '/learn/vectors/magnitude-revisited'
              },
              {
                text: 'Cosine similarity',
                link: '/learn/vectors/cosine-similarity'
              }
            ]
          },
          {
            text: 'Orthogonality',
            link: '/learn/vectors/orthogonality'
          }
        ]
      },
      {
        text: 'Geometry',
        collapsed: true,
        items: [
          {
            text: 'Volumes',
            link: '/learn/geometry/volumes',
            items: [
              {
                text: 'Parallelograms',
                link: '/learn/geometry/parallelograms'
              },
              {
                text: 'Parallelpipeds',
                link: '/learn/geometry/parallelepipeds'
              },
              {
                text: 'Parallelotopes',
                link: '/learn/geometry/parallelotopes'
              }
            ]
          },
          {
            text: 'Normal vectors',
            link: '/learn/geometry/cross-product',
            items: [
              {
                text: 'Area property',
                link: '/learn/geometry/cross-product-area'
              },
              {
                text: 'Triple product',
                link: '/learn/geometry/triple-product'
              }
            ]
          },
          {
            text: 'Areas'
          },
          {
            text: 'Planes',
            link: '/learn/geometry/planes'
          },
          {
            text: 'Plane through three points',
            link: '/learn/geometry/plane-through-three-points'
          },
          {
            text: 'Vector projections',
            link: '/learn/geometry/vector-projections'
          }
        ]
      },
      {
        text: 'Matrices',
        collapsed: true,
        items: [
          {
            text: 'Rows and columns',
            link: '/learn/matrices/rows-and-columns'
          },
          {
            text: 'Transposition',
            link: '/learn/matrices/matrix-transpose'
          },
          {
            text: 'Transforming vectors',
            link: '/learn/matrices/transforming-vectors'
          },
          {
            text: 'Identity matrix',
            link: '/learn/matrices/identity-matrix'
          },
          {
            text: 'Matrix addition',
            link: '/learn/matrices/matrix-addition'
          },
          {
            text: 'Scaling matrices',
            link: '/learn/matrices/scaling-matrices'
          },
          {
            text: 'Matrix composition',
            link: '/learn/matrices/matrix-composition'
          },
          {
            text: 'Determinants in 2D',
            link: '/learn/matrices/determinants-2d'
          },
          {
            text: 'Determinants in 3D',
            link: '/learn/matrices/determinants-3d'
          }
        ]
      },
      {
        text: 'Linear algebra',
        collapsed: true,
        items: [
          {
            text: 'Linear combinations',
            link: '/learn/linear-algebra/linear-combinations'
          },
          {
            text: 'Linear transformations',
            link: '/learn/linear-algebra/linear-transformations'
          },
          {
            text: 'Coming soon'
          }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/nimonian/swe2ml-web' }
    ]
  }
})
