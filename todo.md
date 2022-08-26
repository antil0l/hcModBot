```json
---
-[ ]

Description: This will change your nickname color

Usage:
API: { cmd: 'changecolor', color: '<new color as hex>' }
Text: /color <new color as hex>
Removal: /color reset

---
-[ ]

Description: This will change your current connections nickname

Usage:
API: { cmd: 'changenick', nick: '<new nickname>' }
Text: /nick <new nickname>

---
-[ ]

Description: Broadcasts passed text field to the calling users channel

Usage:
API: { cmd: 'chat', text: '<text to send>' }
Text: Uuuuhm. Just kind type in that little box at the bottom and hit enter.

Bonus super secret hidden commands:
/myhash

---
-[ ]

Description: Typical emote / action text

Usage:
API: { cmd: 'emote', text: '<emote/action text>' }
Text: /me <emote/action text>

---
-[ ]

Description: Outputs information about the servers current protocol

Usage:
API: { cmd: 'help', command: '<optional command name>' }
Text: /help <optional command name>

---
-[ ]

Description: Sends an invite to the target client with the provided channel, or a random channel.

Usage:
API: { cmd: 'invite', nick: '<target nickname>', to: '<optional destination channel>' }

---
-[X]

Description: Join the target channel using the supplied nick and password

Usage:
API: { cmd: 'join', nick: '<your nickname>', pass: '<optional password>', channel: '<target channel>' }

---
-[ ]

Description: Sends back current server stats to the calling client

Usage:
API: { cmd: 'morestats' }
Text: /stats

---
-[ ]

Description: This will change your current channel to the new one provided

Usage: API: { cmd: 'move�, channel: '<target channel>' }
Text: /move <new channel>

---
-[ ]

Description: This module is only in place to supress error notices legacy sources may get

Usage: ping

---
-[ ]

Description: Restore previous state by session id or return new session id (currently unavailable)

Usage:
API: { cmd: 'session', id: '<previous session>' }

---
-[ ]

Description: Sends back legacy server stats to the calling client

Usage:
API: { cmd: 'stats' }

---
-[ ]

Description: Display text on targets screen that only they can see

Usage:
API: { cmd: 'whisper', nick: '<target name>', text: '<text to whisper>' }
Text: /whisper <target name> <text to whisper>
Text: /w <target name> <text to whisper>
Alt Text: /reply <text to whisper, this will auto reply to the last person who whispered to you>
Alt Text: /r <text to whisper, this will auto reply to the last person who whispered to you>

---
-[ ]

Description: Toggle unauthorized trips from interacting with bots. Optional "prepender" field (string) will override default of null char. Optional "reject" field (boolean) will prevent their attempt from being broadcast (default is false).

Usage:
API: { cmd: 'anticmd', prepender: '<optional string>', reject: <optional boolean> }

---
-[ ]

Description: Allow trip through channel locks, captchas, etc

Usage:
API: { cmd: 'authtrip', trip: '<target trip>' }

---
-[ ]

Description: Disconnects the target nickname in the same channel as calling socket & adds to ratelimiter

Usage:
API: { cmd: 'ban', nick: '<target nickname>' }

---
-[ ]

Description: Remove trip from being allowed through channel locks, captchas, etc

Usage:
API: { cmd: 'deauthtrip', trip: '<target trip>' }

---
-[ ]

Description: Disables the captcha in the current channel you are in

Usage:
API: { cmd: 'disablecaptcha' }

---
-[ ]

Description: Globally shadow mute a connection. Optional allies array will see muted messages.

Usage:
API: { cmd: 'dumb', nick: '<target nick>', allies: ['<optional nick array>', …] }

---
-[ ]

Description: Enables a captcha in the current channel you are in

Usage:
API: { cmd: 'enablecaptcha' }

---
-[ ]

Description: Forces a user nick to become a certain color

Usage:
API: { cmd: 'forcecolor', nick: '<target nick>', color: '<color as hex>' }
Text: /forcecolor <target nick> <color as hex>

---
-[ ]

Description: Silently forces target client(s) into another channel. nick may be string or array of strings

Usage:
API: { cmd: 'kick', nick: '<target nick>', to: '<optional target channel>' }

---
-[ ]

Description: Lock the current channel you are in

Usage:
API: { cmd: 'lockroom' }

---
-[ ]

Description: This will move the target user nick into another channel

Usage:
API: { cmd: 'moveuser', nick: '<target nick>', channel: '<new channel>' }

---
-[ ]

Description: Just a test

Usage:
API: { cmd: 'overflow', nick: '<target nickname>' 

---
-[ ]

Description: Pardon a dumb user to be able to speak again

Usage:
API: { cmd: 'speak', ip/hash: '<target ip or hash' }

---
-[ ]

Description: Removes target ip from the ratelimiter

Usage:
API: { cmd: 'unban', ip/hash: '<target ip or hash>' }

---
-[ ]

Description: Clears all banned ip addresses

Usage:
API: { cmd: 'unbanall' }

---
-[ ]

Description: Unlock the current channel you are in or target channel as specified

Usage:
API: { cmd: 'unlockroom', channel: '<optional target channel>' }

---
-[ ]

Description: UwU W-whats thwis?

Usage:
API: { cmd: 'uwuify', nick: '<target nick>' }
```