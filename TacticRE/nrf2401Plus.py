spiPacketLookupTable = {
    0x00: [0xE0, "READ_REGISTER"],
    0x20: [0xE0, "WRITE_REGISTER"],  # first 5 bits are register address
    0x61: [0xFF, "READ_RX_PAYLOAD"],
    0xA0: [0xFF, "WRITE_TX_PAYLOAD"],
    0xE1: [0xFF, "FLUSH_TX"],
    0xE2: [0xFF, "FLUSH_RX"],
    0xE3: [0xFF, "REUSE_TX_PL"],
    0x60: [0xFF, "READ_RX_PL_WID"],  # read rx payload in the rx fifo
    0xA1: [0xF8, "WRITE_TX_ACK_PAYLOAD"],  # stream is frist 3 bits write payload and ack
    0xB0: [0xFF, "WRITE_TX_NAK_PAYLOAD"],
    0xFF: [0xFF, "NOP"]
}

registerAddresses = {
    0x00: "CONFIG",
    0x01: "EN_AA",
    0x02: "EN_RXADDR",
    0x03: "SETUP_AW",
    0x04: "SETUP_RETR",
    0x05: "RF_CH",
    0x06: "RF_SETUP",
    0x07: "STATUS",
    0x08: "OBSERVE_TX",
    0x09: "RPD",
    0x0a: "RX_ADDR_P0",
    0x0b: "RX_ADDR_P1",
    0x0c: "RX_ADDR_P2",
    0x0d: "RX_ADDR_P3",
    0x0e: "RX_ADDR_P4",
    0x0f: "RX_ADDR_P5",
    0x10: "TX_ADDR",
    0x11: "RX_PW_P0",
    0x12: "RX_PW_P1",
    0x13: "RX_PW_P2",
    0x14: "RX_PW_P3",
    0x15: "RX_PW_P4",
    0x16: "RX_PW_P5",
    0x17: "FIFO_STATUS",
    0x18: "",
    0x19: "",
    0x1A: "",
    0x1B: "",
    0x1C: "DYNPD",
    0x1D: "FEATURE",
}
