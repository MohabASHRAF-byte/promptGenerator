module.exports = {
  makers: [
    {
      name: '@electron-forge/maker-squirrel', // Keep this for Windows if you want cross-platform support
      config: {}
    },
    {
      name: '@electron-forge/maker-zip', // Add this for Linux (creates a .zip file)
      platforms: ['linux']
    }
    // Optionally, add maker-deb for .deb packages
    // {
    //   name: '@electron-forge/maker-deb',
    //   config: {}
    // }
  ],
  packagerConfig: {
    asar: true,
    extraResource: [
      '../backend/dist/server'
    ]
  }
};