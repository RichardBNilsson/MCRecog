package com.mco.mcrecog.network;

import com.mco.mcrecog.MCRecog;
import net.minecraft.resources.ResourceLocation;
import net.minecraftforge.network.NetworkRegistry;
import net.minecraftforge.network.simple.SimpleChannel;

public class RecogPacketHandler {
	private RecogPacketHandler() {}

	private static final String PROTOCOL_VERSION = "1";

	private static SimpleChannel INSTANCE;

	public static void init() {
		INSTANCE = NetworkRegistry.newSimpleChannel(
				new ResourceLocation(MCRecog.MODID, "main"),
				() -> PROTOCOL_VERSION,
				PROTOCOL_VERSION::equals,
				PROTOCOL_VERSION::equals);

		int index = 0;

		// Client -> Server
		INSTANCE.registerMessage(index++, ServerboundKeyUpdatePacket.class, ServerboundKeyUpdatePacket::encode,
				ServerboundKeyUpdatePacket::new, ServerboundKeyUpdatePacket::handle);
	}

	public static <MSG> void sendToServer(MSG message) {
		INSTANCE.sendToServer(message);
	}
}
